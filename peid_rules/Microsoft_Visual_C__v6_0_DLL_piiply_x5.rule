rule _Microsoft_Visual_C__v6_0_DLL_piiply
{
	meta:
		description = "Microsoft Visual C__ v6_0 DLL"
	strings:
		$a = {833DB4????????558BEC5657756B6800010000E8??0B000083C4048B7508A3B4??????85F67423837D0C03771D68FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
