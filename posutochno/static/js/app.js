const Index = {
    data() {
        return {
            title: 'Каталог квартир',
            kvartiri: [],
            pag: {
                next: '',
                previous: ''
            },
            listCount: 5
        }
    },
    methods: {
        //     Получаем данные от API

    },
    computed: {
        //     сюда надо получать данные для запроса от inputs
    },
    watch: {

    },
    created: function () {
        const vm = this
        axios.get('api/')
            .then(function (response) {
                vm.kvartiri = response.data.results
            })
    },
}

if (document.getElementById('app')) {
    Vue.createApp(Index).mount('#app')
}
