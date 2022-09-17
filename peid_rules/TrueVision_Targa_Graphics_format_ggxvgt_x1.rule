rule _TrueVision_Targa_Graphics_format_ggxvgt
{
	meta:
		description = "TrueVision Targa Graphics format"
	strings:
		$a = {0000020000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
