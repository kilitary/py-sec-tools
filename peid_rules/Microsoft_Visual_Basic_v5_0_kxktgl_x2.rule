rule _Microsoft_Visual_Basic_v5_0_kxktgl
{
	meta:
		description = "Microsoft Visual Basic v5_0"
	strings:
		$a = {68????????E8????????00000000000030000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
