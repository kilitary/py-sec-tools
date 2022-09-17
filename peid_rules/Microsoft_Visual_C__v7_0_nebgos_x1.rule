rule _Microsoft_Visual_C__v7_0_nebgos
{
	meta:
		description = "Microsoft Visual C__ v7_0"
	strings:
		$a = {558BEC538B5D08568B750C85F6578B7D10}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
