rule _Microsoft_Visual_C__v6_0_DLL_fyshft
{
	meta:
		description = "Microsoft Visual C__ v6_0 DLL"
	strings:
		$a = {0000000000000000????????????????000000004C6F61644C6962726172794100005669727475616C416C6C6F63004B45}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
