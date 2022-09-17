rule _Krypton_v0_5_igrvjz
{
	meta:
		description = "Krypton v0_5"
	strings:
		$a = {5550E8????????5DEB01E360E803??????D2EB0B58EB014840EB01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
