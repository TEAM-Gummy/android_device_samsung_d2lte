$(call inherit-product, device/samsung/d2lte/full_d2lte.mk)

# Enhanced NFC
$(call inherit-product, vendor/Gummy/config/nfc_enhanced.mk)

# Inherit some common Gummy stuff.
$(call inherit-product, vendor/Gummy/config/common_full_phone.mk)

PRODUCT_NAME := tg_d2lte


