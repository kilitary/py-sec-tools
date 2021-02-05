rule _Sexe_Crypter_1_1__by_santasdad_iezevv
{
	meta:
		description = "Sexe Crypter 1_1 _ by santasdad"
	strings:
		$a = {558BEC83C4EC53565733C08945ECB8D8390010E830FAFFFF33C05568D43A001064FF306489????????E43A0010A10057001050E8CCFAFFFF8BD853A10057001050E8FEFAFFFF8BF853A10057001050E8C8FAFFFF8B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
