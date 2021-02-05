rule _Microsoft_Visual_C__8_0_DLL__pbvpqq
{
	meta:
		description = "Microsoft Visual C__ 8_0 _DLL_"
	strings:
		$a = {4883EC28}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
