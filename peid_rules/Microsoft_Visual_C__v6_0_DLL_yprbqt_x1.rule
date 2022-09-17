rule _Microsoft_Visual_C__v6_0_DLL_yprbqt
{
	meta:
		description = "Microsoft Visual C__ v6_0 DLL"
	strings:
		$a = {558D6C????81EC????????8B45??83F801560F84????????85C00F84}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
