import os
import sys
import click


CONTAINER_TEMPLATE = """import React from 'react';
import { connect } from 'react-redux';


const Comp = props => {
    return render(
        <div></div>
    );
};


const mapStateToProps = state => ({});

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Comp);

"""


COMPONENT_TEMPLATE = """import React from 'react';
import PropTypes from 'prop-types';


const {component_name} = props => {{
    return render(
        <div></div>
    );
}};

{component_name}.propTypes = {{}};

{component_name}.defaultProps = {{}};

export default {component_name};

"""


DEFAULT_CONTAINER_FOLDER = 'containers'

DEFAULT_COMPONENT_FOLDER = 'components'


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
def container(name):
    """Create a redux connected container."""
    cwd = os.getcwd()
    write_path = os.path.join(cwd, DEFAULT_CONTAINER_FOLDER, '{name}.jsx'.format(name=name))
    if not os.path.exists(os.path.dirname(write_path)):
        os.mkdir(os.path.dirname(write_path))
    with open(write_path, 'a+') as fl:
        fl.write(CONTAINER_TEMPLATE)


@cli.command()
@click.argument('name')
def component(name):
    """Create a react component."""
    cwd = os.getcwd()
    write_path = os.path.join(cwd, DEFAULT_COMPONENT_FOLDER, '{name}.jsx'.format(name=name))
    if not os.path.exists(os.path.dirname(write_path)):
        os.mkdir(os.path.dirname(write_path))
    with open(write_path, 'a+') as fl:
        fl.write(COMPONENT_TEMPLATE.format(component_name=name))


if __name__ == '__main__':
    pass
