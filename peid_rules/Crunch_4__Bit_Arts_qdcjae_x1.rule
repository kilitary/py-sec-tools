rule _Crunch_4__Bit_Arts_qdcjae
{
	meta:
		description = "Crunch 4 __ Bit_Arts"
	strings:
		$a = {EB100000000000000000000000000000000055E800000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
