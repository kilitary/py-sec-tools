rule _AutoLogic_Graphics_format_urpxvc
{
	meta:
		description = "AutoLogic Graphics format"
	strings:
		$a = {FF040007}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
