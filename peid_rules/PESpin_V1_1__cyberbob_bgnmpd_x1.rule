rule _PESpin_V1_1__cyberbob_bgnmpd
{
	meta:
		description = "PESpin V1_1 __ cyberbob"
	strings:
		$a = {EB016860E8000000008B1C2483C312812BE8B10600FE4BFD822C247DDE46000BE4749E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
