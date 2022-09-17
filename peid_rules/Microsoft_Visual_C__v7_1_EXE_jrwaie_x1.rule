rule _Microsoft_Visual_C__v7_1_EXE_jrwaie
{
	meta:
		description = "Microsoft Visual C__ v7_1 EXE"
	strings:
		$a = {6A??68??????01E8????000066813D000000014D5A75??A13C000001????00000001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
