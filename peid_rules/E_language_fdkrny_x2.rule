rule _E_language_fdkrny
{
	meta:
		description = "E language"
	strings:
		$a = {0BD08BDAE80200000040A05AEB019DB880??????EB02CD2003D38D35F400}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
