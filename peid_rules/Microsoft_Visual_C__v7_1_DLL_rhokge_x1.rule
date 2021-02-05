rule _Microsoft_Visual_C__v7_1_DLL_rhokge
{
	meta:
		description = "Microsoft Visual C__ v7_1 DLL"
	strings:
		$a = {558BEC538B5D08568B750C85F6578B7D107509833D????400000EB2683FE01740583FE027522A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
