rule _Microsoft_Visual_Basic_v6_0_DLL_xlvhhi
{
	meta:
		description = "Microsoft Visual Basic v6_0 DLL"
	strings:
		$a = {5A68????????68????????52E9????FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
