rule _Sharp_GPB_Graphics_format_uzzpie
{
	meta:
		description = "Sharp GPB Graphics format"
	strings:
		$a = {4D00000000????????08000000030000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
