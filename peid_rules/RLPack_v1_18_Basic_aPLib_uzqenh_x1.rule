rule _RLPack_v1_18_Basic_aPLib_uzqenh
{
	meta:
		description = "RLPack v1_18 Basic _aPLib"
	strings:
		$a = {60E8000000008B2C2483C4??8DB5210B00008D9DFF02000033FFE89F0100006A??68????????68????????6A00FF95AA0A00008985F90A0000EB1460FFB5F90A0000FF3437FF743704FFD36183C7??833C370075E6}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
