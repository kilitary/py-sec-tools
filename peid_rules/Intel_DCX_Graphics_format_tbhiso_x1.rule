rule _Intel_DCX_Graphics_format_tbhiso
{
	meta:
		description = "Intel DCX Graphics format"
	strings:
		$a = {B168DE3A041000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
