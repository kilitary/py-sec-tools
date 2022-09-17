rule _Microsoft_Visual_C__DLL_skwcdv
{
	meta:
		description = "Microsoft Visual C__ DLL"
	strings:
		$a = {669C60508BD803??6854BC????6A??FF50148BCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
