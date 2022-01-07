
var appAgendaVue= new Vue ({

	el:'#appAgendaVue',
	data:{

		nuevoContacto: { nombre: '', email: '', telefono:'' },
		contactos:[

			{
				nombre: 'Naroa Jauregi',
				email: 'naroa.jauregi@opendeusto.es',
				telefono: 688866657

			}
		]

	},

	computed:{

		reversedContacts(){

			return this.contactos.slice(0).reverse();
		}
	},

	methods:{

		guardarContacto: function(event){

			this.contactos.push ( { nombre: this.nuevoContacto.nombre, email: this.nuevoContacto.email, telefono: this.nuevoContacto.telefono });
			this.nuevoContacto= { nombre: '', email: '', telefono: ''};
		},
		borrarContacto: function (index){

			this.contactos.splice(index, 1);
		}
	}



})