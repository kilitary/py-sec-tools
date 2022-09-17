rule _Microsoft_Visual_C__v7_0_xyssid
{
	meta:
		description = "Microsoft Visual C__ v7_0"
	strings:
		$a = {6A??68????????E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
