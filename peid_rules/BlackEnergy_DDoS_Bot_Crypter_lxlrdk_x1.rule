rule _BlackEnergy_DDoS_Bot_Crypter_lxlrdk
{
	meta:
		description = "BlackEnergy DDoS Bot Crypter"
	strings:
		$a = {55????81EC1C0100005356576A04BE0030000056FF35002011136A00E8??030000????83C410??FF897DF40F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
