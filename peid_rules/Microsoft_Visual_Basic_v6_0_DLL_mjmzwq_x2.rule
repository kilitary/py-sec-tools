rule _Microsoft_Visual_Basic_v6_0_DLL_mjmzwq
{
	meta:
		description = "Microsoft Visual Basic v6_0 DLL"
	strings:
		$a = {5589E583EC0883C4F46A02A1C8??????FFD0E8????????C9C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
