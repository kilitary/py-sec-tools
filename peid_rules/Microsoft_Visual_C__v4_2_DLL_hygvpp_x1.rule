rule _Microsoft_Visual_C__v4_2_DLL_hygvpp
{
	meta:
		description = "Microsoft Visual C__ v4_2 DLL"
	strings:
		$a = {668BC08D2424EB01EB60EB01EB9CE8000000005E83C6508BFE687801????59EB01EBAC54E803??????5CEB08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
