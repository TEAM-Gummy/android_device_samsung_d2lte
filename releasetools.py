"""Custom OTA commands for Samsung d2 devices """

def FullOTA_InstallEnd(info):
	info.script.AppendExtra('ifelse(is_substring("I747", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_att/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("I747", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_att/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530C", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530C", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530M", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530M", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("L710V", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_spr/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("L710V", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_spr/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("L710W", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_spr/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("L710W", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_spr/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("T999", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_tmo/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("T999", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_tmo/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530U", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("R530U", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_r530/libril.so /system/lib/libril.so"));')
	info.script.AppendExtra('ifelse(is_substring("I535", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_vzw/libril-qc-qmi-1.so /system/lib/libril-qc-qmi-1.so"));')
	info.script.AppendExtra('ifelse(is_substring("I535", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/lib_vzw/libril.so /system/lib/libril.so"));')
