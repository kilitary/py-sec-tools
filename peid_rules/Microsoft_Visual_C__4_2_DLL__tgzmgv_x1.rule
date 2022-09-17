rule _Microsoft_Visual_C__4_2_DLL__tgzmgv
{
	meta:
		description = "Microsoft Visual C__ 4_2 _DLL_"
	strings:
		$a = {53B8????????8B??????565785DB5575}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
