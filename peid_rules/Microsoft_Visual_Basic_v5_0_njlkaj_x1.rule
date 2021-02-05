rule _Microsoft_Visual_Basic_v5_0_njlkaj
{
	meta:
		description = "Microsoft Visual Basic v5_0"
	strings:
		$a = {??????????????FFFFFF0000000000003000000040000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
