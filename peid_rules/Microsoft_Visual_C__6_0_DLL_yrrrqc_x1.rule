rule _Microsoft_Visual_C__6_0_DLL_yrrrqc
{
	meta:
		description = "Microsoft Visual C__ 6_0 DLL"
	strings:
		$a = {558BEC538B5D08568B750C578B7D1085F67509833D??????????EB2683FE01740583FE027522A1????????85C07409575653FFD085C0740C575653E815FFFFFF85C0750433C0EB4E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
