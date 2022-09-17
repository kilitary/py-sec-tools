rule _Microsoft_Visual_C__8_0_MFC__bseebq
{
	meta:
		description = "Microsoft Visual C__ 8_0 _MFC_"
	strings:
		$a = {4883EC28E8????00004883C428E90EFDFFFFCCCCCCCCCCCCCCCCCCCCCCCCCCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
