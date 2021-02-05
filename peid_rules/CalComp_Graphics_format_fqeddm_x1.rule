rule _CalComp_Graphics_format_fqeddm
{
	meta:
		description = "CalComp Graphics format"
	strings:
		$a = {02500A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
