rule _MicroJoiner_1_7__coban2k_zjpiun
{
	meta:
		description = "MicroJoiner 1_7 __ coban2k"
	strings:
		$a = {BF001040008D5F216A0A586A04596057E88E000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
