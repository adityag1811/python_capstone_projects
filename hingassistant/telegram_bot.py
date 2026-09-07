import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

from excel_reader import get_ingredients, get_cost
from calculate_quantity import calculate_quantity
import openpyxl


# -------------------------
# Load Telegram token
# -------------------------

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")


# -------------------------
# Load Excel workbook
# -------------------------

wb = openpyxl.load_workbook(
    "formula.xlsx",
    data_only=True
)


# -------------------------
# Conversation states
# -------------------------

PRODUCT, QUANTITY = range(2)


# -------------------------
# Start conversation
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Which product would you like to calculate?"
    )

    return PRODUCT


# -------------------------
# Receive product
# -------------------------

async def get_product(update: Update, context: ContextTypes.DEFAULT_TYPE):

    product_name = update.message.text

    # Check whether product exists
    if product_name not in wb.sheetnames:

        await update.message.reply_text(
            "Please enter a valid product name."
        )

        return PRODUCT

    # Store product for the next step
    context.user_data["product_name"] = product_name

    await update.message.reply_text(
        "How many kg would you like?"
    )

    return QUANTITY


# -------------------------
# Receive quantity
# -------------------------

async def get_quantity(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        required_qty = int(update.message.text)

    except ValueError:

        await update.message.reply_text(
            "Please enter a valid whole number."
        )

        return QUANTITY

    if required_qty <= 0:

        await update.message.reply_text(
            "Please enter a quantity greater than zero."
        )

        return QUANTITY

    # Retrieve product saved during previous step
    product_name = context.user_data["product_name"]

    # Get worksheet
    product_sheet = wb[product_name]

    # Get last row
    last_row = product_sheet.max_row

    # Get original finished batch quantity
    batch_qty = product_sheet.cell(
        row=1,
        column=13
    ).value

    # Calculate scaling factor
    scaling_factor = required_qty / batch_qty

    # Read formulation
    ingredients = get_ingredients(
        product_sheet,
        last_row
    )

    # Get net cost per kg
    product_costing = get_cost(
        product_sheet,
        last_row
    )

    # Calculate Step 1, Step 2 and Step 3 quantities
    step_1, step_2, step_3 = calculate_quantity(
        ingredients,
        scaling_factor
    )

    # -------------------------
    # Prepare response
    # -------------------------

    response = f"""
Product: {product_name}
Required Quantity: {required_qty} kg

Step 1
"""

    for key, value in step_1.items():

        response += f"\n{key}: {value} Kg"

    if step_2:

        response += "\n\nStep 2"

        for key, value in step_2.items():

            response += f"\n{key}: {value} Kg"

    if step_3:

        response += "\n\nStep 3"

        for key, value in step_3.items():

            response += f"\n{key}: {value} Kg"

    response += f"\n\nNet Cost: ₹{product_costing} per kg"

    await update.message.reply_text(response)

    return ConversationHandler.END


# -------------------------
# Cancel conversation
# -------------------------

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Calculation cancelled."
    )

    return ConversationHandler.END


# -------------------------
# Create Telegram application
# -------------------------

app = ApplicationBuilder().token(bot_token).build()


# -------------------------
# Conversation handler
# -------------------------

conversation_handler = ConversationHandler(

    entry_points=[
        CommandHandler("start", start)
    ],

    states={

        PRODUCT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_product
            )
        ],

        QUANTITY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_quantity
            )
        ]
    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)


# -------------------------
# Register conversation
# -------------------------

app.add_handler(conversation_handler)


# -------------------------
# Start bot
# -------------------------

app.run_polling()