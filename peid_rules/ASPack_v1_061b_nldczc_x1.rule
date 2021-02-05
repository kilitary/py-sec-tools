rule _ASPack_v1_061b_nldczc
{
	meta:
		description = "ASPack v1_061b"
	strings:
		$a = {60E8????????5D81EDEAA843??B8E4A843??03C52B8578AD43??898584AD43??80BD6EAD43}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
