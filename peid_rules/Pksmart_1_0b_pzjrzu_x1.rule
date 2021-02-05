rule _Pksmart_1_0b_pzjrzu
{
	meta:
		description = "Pksmart 1_0b"
	strings:
		$a = {BA????8CC88BC803C281??????51B9????511E8CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
