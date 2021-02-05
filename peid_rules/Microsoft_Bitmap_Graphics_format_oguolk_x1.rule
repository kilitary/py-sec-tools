rule _Microsoft_Bitmap_Graphics_format_oguolk
{
	meta:
		description = "Microsoft Bitmap Graphics format"
	strings:
		$a = {01000900}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
