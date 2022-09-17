rule _Virtual_Image_Maker_Graphics_file_mjmnvt
{
	meta:
		description = "Virtual Image Maker Graphics file"
	strings:
		$a = {534F4D56}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
