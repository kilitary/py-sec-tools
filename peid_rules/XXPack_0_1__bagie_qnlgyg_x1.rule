rule _XXPack_0_1__bagie_qnlgyg
{
	meta:
		description = "XXPack 0_1 __ bagie"
	strings:
		$a = {E8040000008360EB0C5DEB054555EB04B8EBF900C3E8000000005DEB010081ED5E1F4000EB0283098DB5EF1F4000EB028309BAA3110000EB006800??????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
