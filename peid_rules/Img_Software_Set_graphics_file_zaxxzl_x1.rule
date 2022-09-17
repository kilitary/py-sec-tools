rule _Img_Software_Set_graphics_file_zaxxzl
{
	meta:
		description = "Img Software Set graphics file"
	strings:
		$a = {53434D49202020314154}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
