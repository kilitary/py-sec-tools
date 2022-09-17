rule _Microsoft_Visual_C__v6_0_DLL_vzrwji
{
	meta:
		description = "Microsoft Visual C__ v6_0 DLL"
	strings:
		$a = {558BEC538B5D08568B750C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
