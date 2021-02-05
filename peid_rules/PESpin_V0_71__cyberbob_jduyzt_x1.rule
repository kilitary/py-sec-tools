rule _PESpin_V0_71__cyberbob_jduyzt
{
	meta:
		description = "PESpin V0_71 __ cyberbob"
	strings:
		$a = {EB016860E8000000008B1C2483C312812BE8B10600FE4BFD822C2483D546000BE4749E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
