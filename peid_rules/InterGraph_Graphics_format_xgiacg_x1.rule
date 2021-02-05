rule _InterGraph_Graphics_format_xgiacg
{
	meta:
		description = "InterGraph Graphics format"
	strings:
		$a = {0809FE0118000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
