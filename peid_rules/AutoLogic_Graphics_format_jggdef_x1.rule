rule _AutoLogic_Graphics_format_jggdef
{
	meta:
		description = "AutoLogic Graphics format"
	strings:
		$a = {FF040007}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
