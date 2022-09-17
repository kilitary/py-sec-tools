rule _GIF87a_Graphics_format_pmlehg
{
	meta:
		description = "GIF87a Graphics format"
	strings:
		$a = {474946383761}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
