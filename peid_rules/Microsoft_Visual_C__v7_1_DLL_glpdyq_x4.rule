rule _Microsoft_Visual_C__v7_1_DLL_glpdyq
{
	meta:
		description = "Microsoft Visual C__ v7_1 DLL"
	strings:
		$a = {558BEC6AFF68????????68????????64A100000000506489250000000083C4E45356578965E8C745E401000000C745FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
