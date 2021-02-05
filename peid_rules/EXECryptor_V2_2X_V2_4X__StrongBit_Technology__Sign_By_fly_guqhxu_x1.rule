rule _EXECryptor_V2_2X_V2_4X__StrongBit_Technology__Sign_By_fly_guqhxu
{
	meta:
		description = "EXECryptor V2_2X_V2_4X __ StrongBit Technology _ Sign_By_fly"
	strings:
		$a = {E8????????05????????FFE0E8????????05????????FFE0E804000000FFFFFFFF5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
