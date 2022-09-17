rule _Themida_1_0_x_x__1_8_0_0_compressed_engine___Oreans_Technologies_twvdbt
{
	meta:
		description = "Themida 1_0_x_x _ 1_8_0_0 _compressed engine_ __ Oreans Technologies"
	strings:
		$a = {B8????????600BC07458E8000000005805430000008038E9750361EB35E800000000582500F0FFFF33FF66BB195A6683C33466391875120FB7503C03D0BBE944000083C367391A74072D00100000EBDA8BF8B8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
