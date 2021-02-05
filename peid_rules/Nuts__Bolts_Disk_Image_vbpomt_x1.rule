rule _Nuts__Bolts_Disk_Image_vbpomt
{
	meta:
		description = "Nuts _ Bolts Disk Image"
	strings:
		$a = {4E42696D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
