rule _Microsoft_Visual_C__8_jgzsms
{
	meta:
		description = "Microsoft Visual C__ 8"
	strings:
		$a = {E8????0000E9????FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
