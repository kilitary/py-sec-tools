rule _Microsoft_Visual_C__v6_0_DLL_zquldh
{
	meta:
		description = "Microsoft Visual C__ v6_0 DLL"
	strings:
		$a = {8B44??08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
