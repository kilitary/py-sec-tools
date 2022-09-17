rule _ExeShield_Cryptor_1_3RC__Tom_Commander_zrmqlu
{
	meta:
		description = "ExeShield Cryptor 1_3RC __ Tom Commander"
	strings:
		$a = {558BEC53565760E8000000005D81ED8C214000B9512D400081E9E62140008BD581C2E62140008D3A8BF733C0EB0490EB01C2AC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
